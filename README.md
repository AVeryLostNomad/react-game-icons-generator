                         
<br/>
<div align="center">

<h3 align="center">React Game Icons - Generator</h3>
<p align="center">
Generate react-game-icons-auto npm package automatically from a github action with all of the latest icons from game-icons.net

  


</p>
</div>

 ## About The Project

[Game-icons.net](https://game-icons.net) is a treasure trove of high quality and liberally licensed icons for use in all sorts of projects. Traditionally this is games, but several web apps could also benefit from the icons.

There are a few packages on npm that do this (one for svelte and one for react), but all suffer from at least one of a few problems.
- When Game-Icons.net updates, the library does not. Since many of these are created as one-offs for their creator, several of these are more than four years old. That means we're missing a good chunk of new icons.
- Not for react and certainly not for typescript.
- Bad dev experience. Many of React's icon libraries offer search bars on their demo websites (Game-icons.net does similar), but when it comes to the actual files the developer is expected to hardlink imports. This makes it very difficult to make in-app searchbars yourself.

This package aims to be the conclusive, be all end all for solving these problems.

## Features
- Automatically build and deploy a new NPM version of 'react-game-icons-auto' when there are new icons added.
- Collect and export into the built package all 'tags' for icons from the site.
- Provide utility mappings:
  - String icon name to icon ReactNode
  - String tag name to list of string icon names
  - String icon name to list of tags



## Usage / But what about tree shaking?

To import a single icon from game-icons net do:

```typescript
import {PoliceBadge} from "react-game-icons-auto";
```
This should be completely fine. Webpack (or whatever other bundler) will detect you just want a single icon and add only that.

NOTE: Some bundlers appear to not do tree shaking in "dev" mode and save it for production. This means that you could see increased compilation times while it sorts out having all of these four thousand icons in source. 

React-game-icons-auto DOES also export some utility collections which may also be useful to you.
Two are included directly in the base index.ts and can be imported like this
```typescript
import {TagToIconNames, IconNameToTags} from 'react-game-icons-auto';
```
TagToIconNames is a mapping of the various tags on game-icons.net and which icons are within those tags.

IconNameToTags is a mapping of an icon to which tags it has on the site.

Both dictionaries use the string name of the icon as the key.
## Contributing

If there are changes that could make the generated package more support your workflow, feel free to make a PR. 
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
