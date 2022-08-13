# Hexo-plugin-tabs

**Version: 0.01 DEV**

This is a plugin for building styled tabs in hexo.

**Example**:

Not uploaded

**Dependencies: Node.js>=0.10.0, hexo**

- Installation

Simply run "npm install hexo-plugin-tabs" or download the source code and unzip it to "yourwebpage/node_modules/"

```bash
npm install hexo-plugin-tabs
```
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

- Syntax

Example:

```markdown
!!! tabs
++++First tab
First tab section
++++Second tab
Second tab section
++++
```
