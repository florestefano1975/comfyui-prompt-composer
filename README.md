# ComfyUI Prompt Composer

A suite of tools for prompt management.

**_If this project is useful to you and you like it, please consider a small donation to the author._**

➡️ https://ko-fi.com/stefanoflore75

## Overview

![ComfyUI Prompt Composer Node](/screenshot/prompt-composer-overview.png)

Basic workflow for testing the nodes: [prompt-composer-base-workflow.json](/workflow/prompt-composer-base-workflow.json)

## Install from ComfyUI Manager

- Type _florestefano1975_ on the search bar of [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
- Click the install button.

## Manual installation and update instructions

### Install

To install comfyui-prompt-composer:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `git clone https://github.com/florestefano1975/comfyui-prompt-composer`
4. restart ComfyUI

### Update

To update comfyui-prompt-composer:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `cd comfyui-prompt-composer`
4. digit: `git pull`
5. restart ComfyUI

**Warning: update command overwrites files modified and customized by users.**

## Node List

- **Single Text Node**: contains a typing box and a slider to adjust its weight.
- **Multiple Text Node**: contains six typing boxes with sliders to adjust their weights.
- **Styler Node**: style selector from list and slider for set its weight.
- **Effect Node**: effect selector from list and slider for set its weight.
- **Assembler Node**: this node contains six entry points for text strings. The output is a full string prompt.

**Single Text Node**, **Multiple Text Node**, **Styler Node** and **Effect Node** have an entry point (__text_in_opt__) to concatenate unlimitedly with the other nodes.

## Usage

Combining nodes helps the user sequence strings for prompts, also creating logical groupings if necessary. Individual nodes can be chained together in any order.

## Customization

The _lists_ folder contains TXT files with _Style_ and _Effect_ node list entries.

## SDXL Turbo Workflow

In the _workflow_ folder you can download and use an [SDXL Turbo configuration](/workflow/prompt-composer-sdxl-turbo-workflow.json) with some of the custom nodes already inserted and ready to use.

![Styler Node](/screenshot/sdxl-turbo-workflow.png)

## Notes

For advanced photorealism we recommend [FormulaXL 2.0](https://civitai.com/models/129922?modelVersionId=160525).