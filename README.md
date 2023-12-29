# ComfyUI Prompt Composer
A suite of tools for prompt management.

**_If this project is useful to you and you like it, please consider a small donation to the author._**

➡️ https://ko-fi.com/stefanoflore75

## Overview

![ComfyUI Prompt Composer Node](/screenshot/prompt-composer-overview.png)

## Installation and update instructions

### Manual install

To install comfyui-prompt-composer:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `git clone https://github.com/florestefano1975/comfyui-prompt-composer`
4. restart ComfyUI

### Manual update

To update comfyui-prompt-composer:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `cd comfyui-prompt-composer`
4. digit: `git pull`
5. restart ComfyUI

**Warning: update command overwrites files modified and customized by users.**

## Single Text Node

The single text node contains a typing box and a slider to adjust its weight.

![Single Text Node](/screenshot/single-text.png)

## Multiple Text Node

The multiple text node contains six typing boxes with sliders to adjust their weights.

![Multiple Text Node](/screenshot/multiple-text.png)

## Styler Node

The styler node allows you to select a style from a list and set its weight.

![Styler Node](/screenshot/styler.png)

## Effect Node

The effect node allows you to select an effect from a list and set its weight.

![Effect Node](/screenshot/effect.png)

## Assembler Node

The assembly node contains six entry points for text strings. The output is a full string prompt.

![Assembler Node](/screenshot/assembler.png)

## Usage

The combination of nodes helps the user compose their prompt in an orderly and logical way. Visual sliders allow you to conveniently adjust the weight of individual portions of the prompt.

## Customization

The _lists_ folder contains TXT files with _Style_ and _Effect_ node list entries.

## SDXL Turbo Workflow

In the _workflow_ folder you can download and use an SDXL Turbo configuration with some of the custom nodes already inserted and ready to use.

![Styler Node](/screenshot/sdxl-turbo-workflow.png)