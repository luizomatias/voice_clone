# Voice Clone

## About
This repository aims to demonstrate how to use the elevenlabs API to clone your voice and combine with LangChain+ChatGPT so that chatgpt responds with your voice.

## Basic usage:

Fist, make sure you are in a virtual environment. You can use either one (eg virtualenv). Example using conda:

```
conda create -n env python=3.9
conda activate env
```

after that, use makefile command:
* `make deps`: It's gonna install all dependencies you need to run the experiment.

You also need to get the API keys and create an `.env`` file in the root of the project.
 ```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
ELEVEN_API_KEY=<YOUR_ELEVEN_API_KEY>
```

To run de app:
```
make run
``````


## Project Organization
------------

    ├── README.md                          <- The top-level README for developers using this project.
    │
    │   
    │
    │── src                                <- custom source code.
    │   ├── langchain_chatgpt.py           <- function with langchain chatgpt.
    │   ├── voice_clone.py                 <- class VoiceGenerator with elevenlabs API.
    │
    │
    ├── requirements.txt                   <- The requirements file for reproducing the analysis.
    │
    |
    |── main.py                            <- Main file with streamlit app.

--------

## Sources:


<a href="https://docs.elevenlabs.io/api-reference/quick-start/introduction">ElevenLabs Documentation</a>

<a href="https://python.langchain.com/docs/get_started/introduction">LangChain Documentation</a>

<a href="https://docs.streamlit.io/library/get-started">Streamlit Documentation</a>