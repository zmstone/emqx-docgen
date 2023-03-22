# EMQX's document generation

This repo is to hold the generated schema artificats which are used as
the source for documentation rendering.

## Prerequisites

- Erlang/OTP 23.0 or later
- Elixir 1.11.0 or later
- Python 3.6 or later

## How to update

After a new EMQX version 5.x.y is released, execute `gen.sh <version>` to update the content of this repo.

For example, to update the content for v5.0.20, execute:

```bash
./gen v5.0.20 --rebuild
```

The generated content will be placed in the `dist/emqx/v5.0.20` directory.

## Background

The main user interfaces to configure and manage EMQX are

- HTTP API (and on top of it, the web-based dashboard)
- Configuration files
- Command line interface

Starting from version 5, HTTP API and Configuration are developed with
a unified schema to avoid repeating ourselves in:

- Input validation and translation
- Objects and fields documentation

## What is this repo for

For documentation, since the underlying schema is shared,
it is possible to auto-generate them.
E.g. the types and descriptions of the objects and fileds.

However, there are certain parts of the doucment that
are not possible to aut-generate. For example the
lengthy in-general description to explain how the different
configuration system works.

This repo, is created to record the full schema dump and the generated artifacts for each EMQX version starting from v5.0.20.

Including:

- The JSON representation of the schema.
- The hand-crafted document contents, i.e. the parts of the document which do not make sense
  to be a part of [emqx.git](https://github.com/emqx/emqx.git)
- The markdown generation scripts.
