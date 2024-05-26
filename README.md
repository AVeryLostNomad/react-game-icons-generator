                         
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

## But what about tree shaking?

Because the package pulls in (and puts into several data structures) <b>ALL</b> the icons, there is some concern about tree shaking -- or an inability to remove 'dead code'.
For example, if you wanted to use this library and only use one single icon in it, the exported data structures mean that you'd have to pull the whole thing in -- which loads some amount of code you don't need.

Webpack and similar tools *should* be smart enough these days to ignore that if it's not your use case, but please feel free to open an issue to discuss if it's not working for you.

## Contributing

If there are changes that could make the generated package more support your workflow, feel free to make a PR. 
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
