<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/GPT-API/logo.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.2" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=stable&color=green" alt="Version - Stable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
  <a href="https://www.paypal.com/paypalme/gamekdonate">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate" />
  </a>
</div>

<h4 align="center">Python API of ChatGPT3 by OpenAI</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#demo">Demo</a>
</p>

<br>
<br>

## Description

This repository is a complementary library to OpenAI, which adds the GPT3 model.

## Demo

```python
gpt = GPT("API-KEY")
txt = gpt.send("Présent toi")
print(txt)
```

```txt
>>> Je suis une intelligence artificielle créée par OpenAI pour aider les utilisateurs à effectuer diverses tâches et fournir des informations. Je suis programmé pour comprendre plusieurs langages et j'ai accès à une grande quantité de données pour répondre aux requêtes des utilisateurs de manière efficace et précise.
```

```python
gpt = GPT("API-KEY")
txt = gpt.send("Présent toi", onlytext=False)
print(txt)
```

```txt
>>> {
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "\n\nJe suis une intelligence artificielle cr\u00e9\u00e9e par OpenAI. Je suis programm\u00e9e pour r\u00e9pondre aux questions et aider les utilisateurs dans leurs t\u00e2ches quotidiennes. Je peux \u00e9galement communiquer en plusieurs langues et j'apprends constamment \u00e0 partir des interactions avec les utilisateurs.",
        "role": "assistant"
      }
    }
  ],
  "created": 1678177753,
  "id": "chatcmpl-6rMz3wsqTILgbLjiCsruug8QNGL47",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 63,
    "prompt_tokens": 11,
    "total_tokens": 74
  }
}
```
