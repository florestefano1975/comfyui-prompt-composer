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
4. start/restart ComfyUI

### Update

To update comfyui-prompt-composer:

1. open the terminal on the comfyui-prompt-composer folder
2. digit: `cd custom_nodes`
3. digit: `cd comfyui-prompt-composer`
4. digit: `git pull`
5. start/restart ComfyUI

**Warning: before the update create a backup of the TXT files contained in the _custom-list_ folders.**

## Node List

- **Custom Lists Node**: this node reads the lists contained in the _custom-lists_ folder and creates a selector/weight pair for each.
- **Single Text Node**: contains a typing box and a slider to adjust its weight.
- **Multiple Text Node**: contains six typing boxes with sliders to adjust their weights.
- **Grouping Node**: encapsulates the input concatenated strings in brackets () and assigns a weight to the group.
- **Merge Node**: this node joins two text strings.

**Single Text Node**, **Multiple Text Node**, **Styler Node**, **Effect Node** and **Grouping Node** have an entry point (_text_in_opt_) to concatenate unlimitedly with the other nodes, and _active_ switch option for fast by-pass.

## Custom Lists Node

Create the TXT files in the custom-lists folder and insert the selector entries into each of them. You can create lists with simple items or libraries with entire prompts, so you can reuse and combine them as you like.

**Important: changes inserted into the custom lists folder require restarting ComfyUI.**

## Deprecated Nodes

Nodes **Effect** and **Styler** are deprecated and will not receive future updates.

## Usage

Combining nodes helps the user sequence strings for prompts, also creating logical groupings if necessary.

- Individual nodes can be chained together, in any order.
- All _text_outs_ are simple text strings. You can also use nodes with other plugins.
- Slider weights set to 1 do not encapsulate the related text in parentheses ().

## Customization

The _lists_ folder contains TXT files with _Style_ and _Effect_ node list entries.

## SDXL Turbo Workflow

In the _workflow_ folder you can download and use an [SDXL Turbo configuration](/workflow/prompt-composer-sdxl-turbo-workflow.json) with some of the custom nodes already inserted and ready to use.

![Styler Node](/screenshot/sdxl-turbo-workflow.png)

## Notes

For advanced photorealism we recommend [FormulaXL 2.0](https://civitai.com/models/129922?modelVersionId=160525).

## Other projects

- [ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master/)