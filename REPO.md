## Security Weakness Evaluation (w/ Git Hook)
Security of the repository was evaluated with the following pre-commit snippet.

Weaknesses are stored in `bandit.csv`;  the user may abort the commit if any are detected.

  ```
  # Check and record security weaknesses with Bandit
  bandit -f csv -r -o bandit.csv .
  result=$?
  
 # If Bandit recorded security weaknesses, allow the user to abort
  if [ $result -ne 0 ]; then
      read -p "Bandit found security weaknesses. Do you still want to commit? (y/n): " confirm
      if [[ $confirm == [nN] || $confirm == [nN][oO] ]]; then
          echo "Commit aborted."
          exit 1
      fi
  fi
  ```

The following security weaknesses were detected for the given copy of KubeSec (as provided at [continuous-secsoft/sqa2023/project/KubeSec.zip](https://github.com/paser-group/continuous-secsoft/tree/master/sqa2023/project):

|filename           |test_name                           |test_id|issue_severity|issue_confidence|issue_cwe                                      |issue_text                                                                    |line_number|col_offset|end_col_offset|line_range|more_info                                                                                      |
|-------------------|------------------------------------|-------|--------------|----------------|-----------------------------------------------|------------------------------------------------------------------------------|-----------|----------|--------------|----------|-----------------------------------------------------------------------------------------------|
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/helm.values.yaml'                |8          |22        |55            |[8]       |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/tango.values.yaml'               |9          |22        |56            |[9]       |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/charts.values.yaml'              |10         |22        |57            |[10]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/skampi.values.yaml'              |11         |22        |57            |[11]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/minecraft.values.yaml'           |12         |22        |60            |[12]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/kubecf.values.yaml'              |13         |22        |57            |[13]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/nextcloud.values.yaml'           |14         |22        |60            |[14]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/keycloak.values.yaml'            |15         |22        |59            |[15]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/empty.yml'                       |16         |22        |48            |[16]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/kubecf.values.yaml'              |17         |22        |57            |[17]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\TEST_CONSTANTS.py|hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'TEST_ARTIFACTS/special.secret1.yaml'            |106        |22        |59            |[106]     |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\constants.py     |hardcoded_password_string           |B105   |LOW           |MEDIUM          |https://cwe.mitre.org/data/definitions/259.html|Possible hardcoded password: 'Secret'                                         |81         |31        |39            |[81]      |https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html             |
|.\parser.py        |blacklist                           |B404   |LOW           |HIGH            |https://cwe.mitre.org/data/definitions/78.html |Consider possible security implications associated with the subprocess module.|15         |0         |17            |[15]      |https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess|
|.\parser.py        |start_process_with_partial_path     |B607   |LOW           |HIGH            |https://cwe.mitre.org/data/definitions/78.html |Starting a process with a partial executable path                             |332        |25        |106           |[332]     |https://bandit.readthedocs.io/en/1.7.5/plugins/b607_start_process_with_partial_path.html       |
|.\parser.py        |subprocess_without_shell_equals_true|B603   |LOW           |HIGH            |https://cwe.mitre.org/data/definitions/78.html |subprocess call - check for execution of untrusted input.                     |332        |25        |106           |[332]     |https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html  |
|.\parser.py        |start_process_with_partial_path     |B607   |LOW           |HIGH            |https://cwe.mitre.org/data/definitions/78.html |Starting a process with a partial executable path                             |347        |21        |102           |[347]     |https://bandit.readthedocs.io/en/1.7.5/plugins/b607_start_process_with_partial_path.html       |
|.\parser.py        |subprocess_without_shell_equals_true|B603   |LOW           |HIGH            |https://cwe.mitre.org/data/definitions/78.html |subprocess call - check for execution of untrusted input.                     |347        |21        |102           |[347]     |https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html  |

## Implementation of Forensics (logging)
Logging was [implemented](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L20) for five methods to enable forensic analysis of KubeSec.

Methods within `scanner.py` were selecteded for logging as they are referenced directly by main.py (by executing scanner.runScanner).

The logger outputs to `sys.stdout` and `scanner.log`, so that the user may easily reference logs.

\- [`runScanner`](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L668): Log progress information and formatting warnings; relevant print statements replaced with logging.

\- [`getYAMLFiles`](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L79): Log information such as directory contents and path/formatting warnings (Ex. file does not have YAML extension).

\- [`isValidUserName`](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L95): Log validity warnings (Ex. forbidden value) or success information.

\- [`isValidPasswordName`](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L110): Log validity warnings (Ex. incorrect type) or success information.

\- [`isValidKey`](https://github.com/arj0019/JellyfishToast-SQA2023-AUBURN/blob/2769a05c6fe101f7d7a6f425c9b882c7b46d835e/scanner.py#L125): Log validity warnings (Ex. not in 'legit' list) or success information.
