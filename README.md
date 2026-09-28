# <span style="color: #deadff;">🔷 </span> <span style="color: #8b4b5c;">R</span><span style="color: #8b4b5c;">G</span><span style="color: #8b4b5c;">X</span> <span style="color: #deadff;">| </span> <span style="color: #deadff;">L</span><span style="color: #ffffff;">eague of </span><span style="color: #deadff;">L</span><span style="color: #ffffff;">egends </span><span style="color: #deadff;">L</span><span style="color: #ffffff;">evel-</span><span style="color: #deadff;">U</span><span style="color: #ffffff;">p</span><span style="color: #deadff;">!</span>

![LoLLU Logo](media/logo.png)

## ![](media/kiwi.gif) <span style="color: #8b4b5c;">R</span><span style="color: #8b4b5c;">G</span><span style="color: #8b4b5c;">X</span> <span style="color: #4ecdc4;">Mods</span> <span style="color: #3598db;">-</span> <span style="color: #8b4b5c;">R</span><span style="color: #6b8fb0;">ealm</span><span style="color: #8b4b5c;">G</span><span style="color: #8b4b5c;">X</span> <span style="color: #6b8fb0;">Community Project</span>

***

## <span style="color: #deadff;">🎯 Overview</span>

**League of Legends Level-Up! (LOLLU)** replaces World of Warcraft's configured default level-up sound with a League of Legends-inspired chime whenever the player gains a level. It is a small, automatic sound addon built on RGX-Framework.

![RealmGX Kiwi](media/kiwi.gif) **<span style="color: #2dc26b;">The Kiwi Says:</span>** <span style="color: #b96ad9;">"Double kill! Bwwiiiee."</span>

***

## <span style="color: #deadff;">⚠️ Deprecation Notice</span>

<span style="color: #ff6b6b;">**This addon is no longer receiving updates.**</span> Its functionality and League of Legends sound are available in [BLU | Better Level Up!](https://www.curseforge.com/wow/addons/blu-better-level-up) and [BLU Classic | Better Level Up!](https://www.curseforge.com/wow/addons/blu-classic), which combine this sound with a larger sound collection.

Existing standalone users may continue to use this repository as-is, but new installations should prefer the appropriate BLU addon.

***

## <span style="color: #deadff;">✨ Behavior and Features</span>

- Plays the selected League of Legends-inspired sound on `PLAYER_LEVEL_UP`.
- Provides high, medium, and low OGG variants; medium is selected by default.
- Plays through the Master sound channel by default.
- Requests that RGX-Framework mute the configured default level-up sound while LOLLU is enabled.
- Persists enablement and sound-variant choices in `LOLLUSettings`.
- Shows a welcome message on login while that saved preference remains enabled.
- Includes a test command for checking playback immediately.

LOLLU does not alter leveling, experience gains, UI frames, or game data. It only handles the sound associated with the player's level-up event.

***

## <span style="color: #deadff;">🎮 Requirements and Compatibility</span>

`RGX-Framework` is a required dependency and must be installed and enabled. The current TOCs declare these game interfaces:

| WoW flavor | TOC | Interface |
|---|---|---:|
| Retail | `LeagueOfLegendsLevelUp.toc` | `120100` |
| WoW Forever (Beta) | `LeagueOfLegendsLevelUp_Forever.toc` | `16001` |
| Mists of Pandaria Classic | `LeagueOfLegendsLevelUp_Mists.toc` | `50504` |
| Cataclysm Classic | `LeagueOfLegendsLevelUp_Cata.toc` | `40402` |
| Wrath Classic | `LeagueOfLegendsLevelUp_Wrath.toc` | `38002` |
| Burning Crusade Classic | `LeagueOfLegendsLevelUp_TBC.toc` | `20506` |
| Classic Era | `LeagueOfLegendsLevelUp_Vanilla.toc` | `11509` |

These values describe the current release metadata. The addon is deprecated, so they are not a promise of compatibility with later game clients.

***

## <span style="color: #deadff;">📥 Installation</span>

1. Download a packaged release of LeagueOfLegendsLevelUp and install RGX-Framework.
2. Extract both addon folders into the WoW client's `Interface/AddOns` directory.
3. Confirm that the folder is named `LeagueOfLegendsLevelUp` rather than a source-archive name.
4. Enable `RGX-Framework` and `League of Legends Level-Up!` at the character-selection AddOns screen.

For the consolidated replacement, install BLU or BLU Classic instead of the standalone addon.

***

## <span style="color: #deadff;">⌨️ Usage and Configuration</span>

LOLLU works automatically once enabled. It has no graphical configuration panel; use `/lollu` commands in chat:

| Command | Result |
|---|---|
| `/lollu` or `/lollu help` | List available commands. |
| `/lollu test` | Play the selected sound variant. |
| `/lollu enable` | Enable replacement playback. |
| `/lollu disable` | Disable replacement playback. |
| `/lollu high` | Select the high-quality file. |
| `/lollu med` or `/lollu medium` | Select the medium-quality file. |
| `/lollu low` | Select the low-quality file. |

The initial defaults are enabled, medium quality, Master-channel playback, default-sound muting, and the welcome message. Settings persist between sessions in `LOLLUSettings`.

***

## <span style="color: #deadff;">🧩 Files and Runtime</span>

- `data/locales.lua` defines chat and welcome text.
- `data/core.lua` registers the sound set, events, saved settings, and `/lollu` command.
- `sounds/league_of_legends_{high,med,low}.ogg` are the active playback files.
- `media/icon.tga`, `media/logo.png`, and `media/kiwi.gif` provide addon and project artwork.

At addon load, LOLLU initializes its RGX-Framework sound handle. At login it displays the optional welcome message. Each later `PLAYER_LEVEL_UP` event plays the selected variant when the addon is enabled, and logout allows the framework handle to finalize its state.

***

## <span style="color: #deadff;">🛠️ Troubleshooting</span>

- If WoW marks LOLLU as missing a dependency, install or enable `RGX-Framework`.
- If no custom sound plays, run `/lollu test`, then `/lollu enable` and select a variant again.
- If the default sound also plays, verify that LOLLU and RGX-Framework both loaded without Lua errors.
- If WoW cannot find the addon, verify the exact `Interface/AddOns/LeagueOfLegendsLevelUp` folder name.

Because the standalone project is retired, migrate to BLU or BLU Classic when you prefer the consolidated sound addon.

***

## <span style="color: #deadff;">🔗 Project Links</span>

- [Repository](https://github.com/RGXMods/LeagueOfLegendsLevelUp)
- [Releases](https://github.com/RGXMods/LeagueOfLegendsLevelUp/releases)
- [Issues](https://github.com/RGXMods/LeagueOfLegendsLevelUp/issues)
- [Author: DonnieDice](https://github.com/donniedice)
- [Support development](https://www.buymeacoffee.com/donniedice)

This repository is retained for existing users and historical context. Issue reports and contributions should account for the deprecation notice and the migration path above.

***

## <span style="color: #4ecdc4;">🌟 Thank you for choosing </span> <span style="color: #8b4b5c;">R</span><span style="color: #8b4b5c;">G</span><span style="color: #8b4b5c;">X</span> <span style="color: #4ecdc4;">Mods! 🌟</span>
