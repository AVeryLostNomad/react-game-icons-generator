                         
<br/>
<div align="center">

<h3 align="center">THIS IS AUTO GENERATED - SEE REPO FOR MORE</h3>
<h3 align="center">React Game Icons - Auto</h3>
<p align="center">
Automatic transpilation of game-icons.net icons into react components with typescript support.


  


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

React-game-icons-auto DOES also export some utility collections which may also be useful to you.
Two are included directly in the base index.ts and can be imported like this
```typescript
import {TagToIconNames, IconNameToTags} from 'react-game-icons-auto';
```
TagToIconNames is a mapping of the various tags on game-icons.net and which icons are within those tags.

IconNameToTags is a mapping of an icon to which tags it has on the site.

The third exported dictionary should be used with caution.
```typescript
import {default as IconNameToReactNode} from 'react-game-icons-auto/nametonode'
```
This dictionary is a mapping of string icon name to its react node representation. It will make any bundler load the entire set of icons into memory, which adds approximately 10-20 MB to your load. 

This is provided because some users may with to design a search functionality that provides ALL the icons as options (my use case) where the initial extra load time is negligible.

## Contributing

If there are changes that could make the generated package more support your workflow, feel free to make a PR. 
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
