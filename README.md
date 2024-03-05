# Introduction:

This is repo that compares the performance of the following:
**GPT-4** vs **Claude 3** in following aspects for GUI application development,
This repo is for the purpose of learning and understanding the performance of the both **LLM**.
And these were tested on platform [Fast-Chat](https://chat.lmsys.org/) to compare both two **LLMs** side by side.

# Applications tests.

- **Video Player** : This is basic video Player that plays the video and it has very basic controls for a video player.

_claud file_: `claude-apps/movie-player.py`</br>
_gpt file_: `gpt-apps/movie-player.py`</br>

- **Download Manager** : This is a basic download manager that downloads the files It shows the information of the file that is downloaded, and it shows the speed and the progress of the download

_claude file_: `claude-apps/download-manager.py`</br>
_gpt file_: `gpt-apps/download-manager.py`</br>

- **Encryptor** : This is a basic encryptor that encrypts the files and decrypts the files. And user can save and load the files aswell.

_claude file_: `claude-apps/basic-encryptor.py`</br>
_gpt file_: `gpt-apps/basic-encryptor.py`</br>

- **File Information** : This is a basic file information that shows the information of the file with advance sections.

_claude file_: `claude-apps/file-informator.py`</br>
_gpt file_: `gpt-apps/file-informator.py`</br>

- **Data Generator**: This is JSON data generator app that generates the JSON data with different sections.

_claude file_:  `claude-apps/data-generator.py`</br>
_gpt file_:  `gpt-apps/data-generator.py`</br>

- **Prime Timer**: This is a prime number timer that shows the prime numbers in countdown timer fashion.

_claude file_: `claude-apps/prime-timer.py`</br>
_gpt file_: `gpt-apps/prime-timer.py`</br>

# Directory Structure.

The directory strucutre is as follows:
- **claude-apps**: It contains all the applications source that were generated by _Claude-3_ latest model.
- **gpt-apps**: It contains all the applications source that were generated by _GPT-4_ latest model.
- **prompts**: It contains all the data for prompts that were given to generate these applications.