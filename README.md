# Auto-Click

**Auto-Click** is a Python utility extracted from the older **CustomKeys** project that automates repeated mouse clicks or keyboard presses.

It provides two input modes:

* **Continuous Mode** – Continuously performs mouse clicks or keyboard presses.
* **Clip Mode** – Limits the number of inputs to simulate a fixed in-game magazine or clip size.

> **Important:** Special keys are **not supported**.

## Features

* Automated mouse clicking
* Automated keyboard input
* Continuous input mode
* Limited-input (clip) mode
* Configurable input delay
* Randomized delay disturbance
* Double-safe key bindings to prevent accidental activation
* Configurable through `config.json`
* Simple console UI
* Optional emoji-based UI for consoles that support emojis

## Requirements

* Python **3.12.6 or higher** when activating the program through a code editor
* `pynput`
* `rich`

Install the required packages with:

```bash id="p6u1va"
pip install pynput rich
```

## Usage

1. Download the project files.
2. Build the program with **PyInstaller**.
3. Run the program for the first time. A `config.json` file will be created.
4. Make sure the **kill switch is off**.
5. Open `config.json` and configure the settings if needed. This step can be skipped if the default settings are suitable.
6. Activate the kill switch to start Auto-Click.

## `config.json` Guide

### `display`

Controls whether the console interface uses emojis or plain text.

### `key_[...]`

Configures the keyboard bindings used by the program.

It is recommended to use at least two keys together for important triggers to prevent accidental activation.

> **Note:** Special keys are not supported.

### `[...]_emoji`

Defines the emoji character used to display the positive or negative state of a switch.

This setting is only useful on consoles that support emojis.

### `key_action`

Displays the keyboard key that will be triggered on the on-screen display.

This setting is used when mouse input is disabled.

> **Note:** On mouse used only **LMB** button! Not configurable!

### `count`

Displays the number of clicks or key presses performed by Auto-Click.

The count is not displayed when **Clip Mode** is disabled.

### `[min/max]_delay`

Sets the minimum and maximum delay between individual clicks or key presses.

The values are specified in **milliseconds**.

For example:

```text id="q08t9n"
min_delay = 100
max_delay = 500
```

The actual delay is randomized between the configured minimum and maximum values.

> **Warning:** Setting the delay too low may result in input being detected as unnatural by some applications or anti-cheat systems.

### `max_disturbance`

Adds a randomized amount of additional time to each input delay.

For every interaction, a new disturbance value is generated between zero and the configured maximum.

The value is specified in **milliseconds**.

For example, if the maximum disturbance is `100`, each interaction may receive an additional random delay of up to 100 milliseconds.

### `clicks_cap`

Sets the maximum number of inputs allowed during **Clip Mode**.

This represents the size of the simulated in-game "magazine" or "clip".

For example:

```text id="bq4d6n"
clicks_cap = 30
```

allows up to 30 clicks or key presses before the clip is considered empty and Auto-Click will stop.

## Project Status

**Finished**
