# Hexo-plugin-tabs


## Introduction
**Version: 0.01 DEV**

This is a plugin for building styled tabs in hexo.

**Example**:

![example1](https://user-images.githubusercontent.com/109156954/184471955-5e90987b-0be7-438f-aca2-6753d776d8d7.jpg)

**Dependencies: Node.js>=0.10.0, hexo, windows (Available for only windows)**

## How to use
- **Installation**

Simply run "npm install hexo-plugin-tabs" or download the source code and unzip it to "yourwebpage/node_modules/"

```bash
npm install hexo-plugin-tabs
```

after every "hexo g" or "hexo s", you will see a "tabs generated successfully" as a result of installation
**or**
```bash
git clone https://github.com/sclass53/hexo-plugin-tabs.git node_modules/hexo-plugin-tabs
```

Then add one line "hexo-plugin-tabs>=0.0.1 "in the "dependencies" of "package.json" of your webpage folder, 

```json
"dependencies":{
  "example>=x.x.x",
  //etc.
  "hexo-plugin-tabs>=0.0.1"
}
```

- **Syntax**

Example:

```markdown
!!! tabs
++++First tab
First tab section
++++Second tab
Second tab section
++++
```

Simply type **!!! tabs** at the section you want to insert tabs, and add "++++tab title 1" to add a tab
Insert tab text between tab markings (aka. ++++).
To end, mark "++++"

It will automatically be converted into html
```html
<iframe src="\httabs\ok.html"></iframe>
```
**Result**:

![example2](https://user-images.githubusercontent.com/109156954/184471961-db3e481c-8138-4bee-b3c0-cf224ec096d2.jpg)

A postname.html will be created under the /source/httabs/ dir (httabs is created after first generating process). Check /bin/source.html for more imformation.

run
```
hexo g
hexo s
```
to test

## License

CC-BY-SA 4.0

## Contributors

@ginoblog, @melvinzhang (not a user)
