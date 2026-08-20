# Front-End Test Assignment

Here lies a description of a test assignment for the position of a Front-End-developer @ KazanExpress.\
If you've discovered it accidentaly - give it a go! We might just hire you after that. 😉

[RU](frontend-test-task.md) | [EN](frontend-test-task-en.md)

## The assignment

Implement a Single Page TODO Application.

The app can be implemented in one of the following difficulty levels:

- [**Easy**](#easy) - submissions are not currently evauated for this difficulty;
- [**Medium**](#medium) - **Easy** with additional complications, minimally-evaluated functionality;
- [**Hard**](#hard) - **Medium** with additional complications;
- [**Insane**](#insane) - the ultimate challenge - we provide a special treatment for those, who complete it!

## Detailed requirements

Below you can find detailed requirements for the assignment, grouped by difficulty.\
Each consecutive difficulty includes **all** requirements of all previous difficulties as required.

---

### **Easy**

- Each new browser tab should be a separate project with its own task list;
- Editable project name that serves as the page's title;
- List of tasks:
  - Add new task to the list;
  - Delete any task from the list;
  - Ability to mark any task as complete/uncomplete;
- All information (project name, list of tasks, each tasks' state) must be preserved upon page reload;

Optional:
- Ability to add subtasks to any task in the list (with potentially infinite depth);
- Ability filter/search tasks using an input field (currently used filter must be preserved upon page reload);
- Ability to edit any task's title after its creation;

---

### **Medium**

All requirements for [**easy**](#easy), including optional.
Also, the following:

- Ability to transfer any task (with all of its substasks) from any open project to any other open project;
- Usage of `LocalStorage`, `Cookies`, `IndexedDB` and `WebSQL` is prohibited;\
  **Any** records in these storages are completely prohibited!\
  This rule also holds for any libraries that use these types of storages.\
  For example - `vuex-multi-tab-state` is prohibited, because it uses `LocalStorage`.
- Ability to export a project to a file / import a project from a file;
  - Name of the file corresponds to the name of the project:
    Project name must be set from the file's name upon import;
    File's name must be set from project's name upon export;
- Move tasks in the task list using drag-n-drop;
- Ability to save current filter for quick-search later;
- Complete application bundle must be below **200 KB** (sum of all files loaded by the browser, excluding pictures and SVGs);

Optional:
- CSS-animated drag-n-drop and task filter (animated list items' movement);
- Use TypeScript for 100% of the code base (excluding markup and styles);
- Use [Vue Composition API](https://vue-composition-api-rfc.netlify.com/) or [vue@next](https://www.npmjs.com/package/vue/v/next);
- Use ESLint/TSLint (usage of [KazanExpress/TSLint](https://github.com/KazanExpress/tslint) is highly encouraged);
- Use a bundler (like [webpack](https://webpack.js.org/)) for bundling the final SPA;

---

### **Hard**

All requirements for [**medium**](#medium), inluding optional and the following:

- Complete application bundle must be below **100 KB** (sum of all files loaded by the browser, excluding pictures and SVGs);
- Move tasks in the task list using drag-n-drop **with touch-screen support**;
- App must be adapted for mobile devices, down to 320x480 (iPhone 4);
- Ability to quickly view and edit a lengthy multi-line description for any task;

Optional:
- [SSR](https://google.com/search?q=SSR+(web+development));
- [PWA](https://google.com/search?q=PWA+(web+development));
- Ability to filter tasks using Regular Expressions;
<!-- - Если в двух вкладках открыт один и тот же проект (например, совершён импорт из одного и того же файла),\
  **все** действия в этих вкладках/проектах должны синхронизироваться без задержки.\
  Включая (но не ограничиваясь):
  - Название проекта;
  - Список, состояния, описания, порядок и названия всех задач\
    (например, при добавлении задачи в одной вкладке - она должна появиться и в другой);
  - Список сохранённых фильтров; -->
- Ability to add/delete named columns for tasks, with ability to move tasks between them ("trello"-like);

---

### **Insane**

> We can only praise your courage and skill, should you decide to complete the assignment at this difficuly. 👏\
> Oh, and hire you, of course!

All requirements for [**hard**](#hard), inluding optional. And the following:

- Usage of `Vue.js` or any other framework/library for the client-side part is **prohibited** - only native JavaScript/TypeScript;\
  Including:
  - Reactivity and data-binding;
  - DOM mutations;
  - Business-logic;
  - And yes, jQuery/React/Lodash/Underscore/Bootstrap are also banned!
- Code documentation using JSDoc;
- Complete application bundle must be below **50 KB** (sum of all files loaded by the browser, excluding pictures and SVGs);
- Final application bundle must work using ES6-modules via `<script type="module">`;
- [Source-Maps](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map) for the bundled app and an instruction on how to use them;
- Full keyboard control support, using hot-keys;
  (provide a complete list of supported hot-keys)
- Code quality rating "**A**" on [Code Climate](https://codeclimate.com) (add a badge to the top of the repo's README);

Optional:
- Use [Conventional Commitlint](https://github.com/conventional-changelog/commitlint);
- Use [CustomElements/WebComponents](https://developer.mozilla.org/en-US/docs/Web/Web_Components) & [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM);
- 100% test coverage using Jest/Mocha and [Coveralls](https://coveralls.io)/[Code Climate](https://codeclimate.com);
- Use travis.ci, [now.sh](https://zeit.co/home), GitHub Pages or GitHub Actions for CI/CD;
- Use [Service-Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) to notify the user of new verions or updates to the app;
- Mutually exclusive requirements:
  - Self-implemented [SSR](https://google.com/search?q=SSR+(web+development)) without using 3rd-party libraries;
  - No SSR **and** no bundler (webpack, rollup, etc.), node_modules or anything - i.e. all libraries (for the sole exclusion of TypeScript and testing frameworks) are banned;


---

Anything that is not stated in the requirements is left up to the creative freedom of the candidate.

It's encouraged to attempt implementation of optional requirements for higher difficulties than your current choice.\
For example, if you've decided to go with **medium** difficulty, implementing optional requirements from **hard** will give you a substantial advantage upon evaluation.

<details><summary>FAQ</summary>

Q: Can't figure out how to implement feature X - tried everything! Can I skip feature X?\
A: All features are possible to implement - we tried it ourselves! The solution is probably waiting for you just around the corner. 😉

Q: Can I skip optional requirements from **easy**, if I'm doing **medium**?\
A: No. All requirements from all previous dificulties are mandatory. They were optional for that previous difficulty, not for your current one.

</details>

---

## Assignment rules

Description **must** contain:
  - A full list of implemented requirements;
  - An instruction on how to run the app locally for Windows/Unix.

## Deadlines

 - 7 days, starting with the receiving the task - for **easy**, **medium** and **hard**.
 - 14 days, starting with the receiving the task - for [**Insane**](#insane) difficulty - not counting the time for implementation of optional requirements.
