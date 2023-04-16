#!/bin/bash

index_file="index.html"

cd "$(dirname "$0")"

cd docs/


gen_lang_list() {
    lang="$1"
    # Find all JSON files in the subdirectories and create a list with links
    find "$lang" -type f -iname "*.json" | while read -r file; do
        echo "<li><a href=\"v.html?s=$file\">$file</a></li>"
    done
}

EN_LIST="$(gen_lang_list en)"
ZH_LIST="$(gen_lang_list zh)"

cat<<EOF > index.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900"/>
  <title>EMQX Config Docs</title>
<style>
  body {
    font-family: 'Roboto', Arial, sans-serif;
  }
  .tab-container {
    display: flex;
    justify-content: flex-start;
  }
  .tab {
    padding: 10px 20px;
    margin-right: 5px;
    border: 1px solid #ccc;
    border-bottom: none;
    border-radius: 5px 5px 0 0;
    background-color: #f1f1f1;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  .tab:hover {
    background-color: #ddd;
  }
  .tab-content-container {
    width: 100%;
  }
  .tab-content {
    display: none;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: white;
  }
  .active {
    background-color: white;
    border-bottom: 1px solid white;
  }
</style>

  <script>
    function switchTab(evt, lang) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tab-content");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      tablinks = document.getElementsByClassName("tab");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
      }
      document.getElementById(lang).style.display = "block";
      evt.currentTarget.classList.add("active");
    }
  </script>
</head>
<body>
  <div class="tab-container">
    <div class="tab active" onclick="switchTab(event, 'English')">English</div>
    <div class="tab" onclick="switchTab(event, 'Chinese')">中文</div>
  </div>
    <div id="English" class="tab-content" style="display: block;">
      <ul>

${EN_LIST}

      </ul>
    </div>
    <div id="Chinese" class="tab-content">
      <ul>

${ZH_LIST}

      </ul>
    </div>
</body>
EOF
