#!/usr/bin/env elixir

Mix.install([
  {:hocon, github: "emqx/hocon"},
  # {:hocon, path: "../hocon/"},
  :jason
])

defmodule Main do
  Code.require_file("md.exs")
  Code.require_file("schema_md.exs")

  defp usage do
    IO.puts "Usage: my_script.exs [--lang=<language>] --outdir=<path>"
    IO.puts "  --lang=<language>  The language to use (default: en)"
    IO.puts "  --outdir=<path>    The output directory (required)"
    IO.puts "                     points to where the json files are located"
    System.halt(1)
  end

  def parse_args!(args) do
    {opts, _} = OptionParser.parse!(args, strict: [lang: :string, outdir: :string])
    lang = opts[:lang]
    outdir = opts[:outdir]
    unless lang in ["en", "zh"] do
      usage()
    end
    unless outdir do
      usage()
    end
    %{lang: lang, outdir: outdir}
  end

  def sections() do
    generic_section = [
      %{
        slug: "others",
        title: "Other Configurations"
      }
    ]

    common_sections = [
      %{
        slug: "emqx",
        title: "EMQX",
      },
      %{
        slug: "authn",
        title: "Authentication"
      },
      %{
        slug: "authz",
        title: "Authorization"
      },
      %{
        slug: "bridges",
        title: "Bridges"
      },
      %{
        slug: "rule",
        title: "Rule Engine"
      },
      %{
        slug: "gateway",
        title: "Gateways"
      }
    ]

    sections_ce = common_sections ++ generic_section

    sections_ee =
      common_sections ++
      [
        %{
          slug: "license",
          title: "License"
        }
      ] ++ generic_section

    %{
      sections_ce: sections_ce,
      sections_ee: sections_ee,
    }
  end

  def make_index(sections, lang) do
    preamble = File.read!("preamble.#{lang}.md")
    entries =
      sections
      |> Enum.map(fn %{slug: slug, title: title} ->
        MD.link(title, "./#{slug}.md")
      end)
      |> MD.ul()

    """
    #{preamble}

    # Sections

    #{entries}
    """
  end

  @doc """
  Creates an index mapping full names to files/sections, as they will
  be cross-referenced by fields/structs in different sections.
  """
  def index_full_names(outdir, sections) do
    for %{slug: slug, title: _title} <- sections,
        %{full_name: full_name} <- read_structs!(outdir, slug),
        reduce: %{} do
      acc ->
          if Map.has_key?(acc, full_name) and acc[full_name] != slug do
            ctx = %{
              full_name: full_name,
              acc: acc,
              slug: slug,
              existing: acc[full_name],
            }
            raise "repeated header! #{inspect(ctx, pretty: true)}"
          end
          Map.put(acc, full_name, slug)
    end
  end

  def read_structs!(dist_dir, slug) do
    [dist_dir, "json", "#{slug}.json"]
    |> Path.join()
    |> File.read!()
    |> Jason.decode!(keys: :atoms)
  end

  def generate_markdown(opts) do
    %{lang: lang, outdir: outdir} = opts
    %{
      sections_ce: sections_ce,
      sections_ee: sections_ee,
    } = sections()

    sections = case String.starts_with?(Path.basename(outdir), "v") do
      true -> sections_ce
      false -> sections_ee
    end
    Enum.each(sections, fn %{slug: slug, title: title} = section ->
      index = make_index(sections, lang)
      outfile = Path.join([outdir, "index.md"])
      File.write!(outfile, index)

      header_index = index_full_names(outdir, sections)
      body = Map.get(section, :body, "")

      md =
        outdir
        |> read_structs!(slug)
        |> SchemaMD.gen_from_structs(%{
            title: "# #{title}",
            body: body,
            env_prefix: "EMQX_",
            header_index: header_index,
            current_slug: slug,
          })

      outfile = Path.join([outdir, "#{slug}.md"])
      File.write!(outfile, md)
    end)
  end

  def main() do
    System.argv()
    |> parse_args!()
    |> generate_markdown()
  end
end

Main.main()
