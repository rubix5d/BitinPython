{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPiSqMbtIUT0SyftcmoTYMN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rubix5d/BitinPython/blob/main/table_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "3JLdtEW6VNVQ",
        "outputId": "ef36d81c-b4e8-46be-e3d8-32e28191c107"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-0aa96786-2ead-474c-bfb2-ac1202237955\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-0aa96786-2ead-474c-bfb2-ac1202237955\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving database.sqlite to database.sqlite\n"
          ]
        }
      ],
      "source": [
        "from google.colab import files\n",
        "file = files.upload()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlite3\n",
        "\n",
        "database = \"database.sqlite\"\n",
        "\n",
        "conn = sqlite3.connect(database)\n",
        "\n",
        "print(\"Successfully connected\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SjzADuHoZtTL",
        "outputId": "258ad7dc-8a14-4f5f-abed-ac6a028e7daa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Successfully connected\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "tables = pd.read_sql(\"\"\"SELECT * FROM sqlite_master\n",
        "                        WHERE type = \"table\";\"\"\", conn)\n",
        "\n",
        "print(tables)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zKKCqPZWabWo",
        "outputId": "76a6bf8a-5a40-4247-f252-1ff3e1328f22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     type             name         tbl_name  rootpage  \\\n",
            "0   table           Player           Player         2   \n",
            "1   table       Extra_Runs       Extra_Runs         3   \n",
            "2   table   Batsman_Scored   Batsman_Scored         7   \n",
            "3   table    Batting_Style    Batting_Style        10   \n",
            "4   table    Bowling_Style    Bowling_Style        11   \n",
            "5   table          Country          Country        12   \n",
            "6   table           Season           Season        14   \n",
            "7   table             City             City        15   \n",
            "8   table          Outcome          Outcome        16   \n",
            "9   table           Win_By           Win_By        17   \n",
            "10  table     Wicket_Taken     Wicket_Taken        18   \n",
            "11  table            Venue            Venue        21   \n",
            "12  table       Extra_Type       Extra_Type        23   \n",
            "13  table         Out_Type         Out_Type        24   \n",
            "14  table    Toss_Decision    Toss_Decision        25   \n",
            "15  table           Umpire           Umpire        26   \n",
            "16  table             Team             Team        27   \n",
            "17  table     Ball_by_Ball     Ball_by_Ball        28   \n",
            "18  table      sysdiagrams      sysdiagrams        31   \n",
            "19  table  sqlite_sequence  sqlite_sequence        32   \n",
            "20  table            Match            Match        34   \n",
            "21  table            Rolee            Rolee        36   \n",
            "22  table     Player_Match     Player_Match        37   \n",
            "\n",
            "                                                  sql  \n",
            "0   CREATE TABLE [Player] (\\n\\t[Player_Id]\\tintege...  \n",
            "1   CREATE TABLE [Extra_Runs] (\\n\\t[Match_Id]\\tint...  \n",
            "2   CREATE TABLE [Batsman_Scored] (\\n\\t[Match_Id]\\...  \n",
            "3   CREATE TABLE [Batting_Style] (\\n\\t[Batting_Id]...  \n",
            "4   CREATE TABLE [Bowling_Style] (\\n\\t[Bowling_Id]...  \n",
            "5   CREATE TABLE [Country] (\\n\\t[Country_Id]\\tinte...  \n",
            "6   CREATE TABLE [Season] (\\n\\t[Season_Id]\\tintege...  \n",
            "7   CREATE TABLE [City] (\\n\\t[City_Id]\\tinteger NO...  \n",
            "8   CREATE TABLE [Outcome] (\\n\\t[Outcome_Id]\\tinte...  \n",
            "9   CREATE TABLE [Win_By] (\\n\\t[Win_Id]\\tinteger N...  \n",
            "10  CREATE TABLE [Wicket_Taken] (\\n\\t[Match_Id]\\ti...  \n",
            "11  CREATE TABLE [Venue] (\\n\\t[Venue_Id]\\tinteger ...  \n",
            "12  CREATE TABLE [Extra_Type] (\\n\\t[Extra_Id]\\tint...  \n",
            "13  CREATE TABLE [Out_Type] (\\n\\t[Out_Id]\\tinteger...  \n",
            "14  CREATE TABLE [Toss_Decision] (\\n\\t[Toss_Id]\\ti...  \n",
            "15  CREATE TABLE [Umpire] (\\n\\t[Umpire_Id]\\tintege...  \n",
            "16  CREATE TABLE [Team] (\\n\\t[Team_Id]\\tinteger NO...  \n",
            "17  CREATE TABLE [Ball_by_Ball] (\\n\\t[Match_Id]\\ti...  \n",
            "18  CREATE TABLE [sysdiagrams] (\\n\\t[name]\\tnvarch...  \n",
            "19             CREATE TABLE sqlite_sequence(name,seq)  \n",
            "20  CREATE TABLE [Match] (\\n\\t[Match_Id]\\tinteger ...  \n",
            "21  CREATE TABLE [Rolee] (\\n\\t[Role_Id]\\tinteger N...  \n",
            "22  CREATE TABLE [Player_Match] (\\n\\t[Match_Id]\\ti...  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "country = pd.read_sql(\"\"\"\n",
        "\n",
        "SELECT * FROM Country\n",
        "WHERE Country_Name LIKE 'S%';\n",
        "\"\"\", conn)\n",
        "\n",
        "print(country)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Cl9iMgwa94C",
        "outputId": "f81c57f2-50c1-4165-a2dc-437f3432db7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Country_Id  Country_Name\n",
            "0           2  South Africa\n",
            "1           7     Sri Lanka\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "venue = pd.read_sql(\"\"\"\n",
        "SELECT MIN(Venue_Name) FROM Venue;\n",
        "\n",
        "\"\"\", conn)\n",
        "\n",
        "print(venue)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yUJRdJJbcSv6",
        "outputId": "c1ac0004-dd24-4e6c-f2fe-1035b78dbd40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    MIN(Venue_Name)\n",
            "0  Barabati Stadium\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Zv3VO8uPdNA9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}