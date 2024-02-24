### Introduction
---
Hi 👋 there, just incase you tumble upon this `repo`. Nothing serious is innit, it's my learning repo for a UI library `Svelte` and how it integrates with my [DJango] `django-rest` sweet pie😘 tech stack. 
Most of it is `spangetti` code. Examples on different implementations which I can only understand. So, _judge ye NOT, lest you'll also be JUDGED `(sic)`_.

> There many sample apps. Mostly diff implementation of TODOS.
>

### Running the apps
1. Backend
`python manage.py runserver`
It'll be serverd on `htpp://127.0.0.1:8000`

#### Get all movies
To test the API, use any api client that works for you. For example `postman` or `Insomnia`.

<!-- ![Build Status](https://github.com/github/docs/actions/workflows/main.yml/badge.svg) -->
[POST|GET|PUT|DELETE] methods
[http://127.0.0.1:8000/api/moviestore/v1/movies/]

2. Frontend
`npm run dev`
Exposed on [http://localhost:5173](http://localhost:5173/)

#### List all movies
1. Run
[http://localhost:5173/movies](http://localhost:5173/movies)

#### List a movie
Steps
[http://localhost:5173/movies/[id]](http://localhost:5173/movies/[id])



### Create-svelte

Everything you need to build a Svelte project, powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm create svelte@latest

# create a new project in my-app
npm create svelte@latest my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.


### Update


### redirect
Use `goto` imported from `{$app/navigation}`

### Assets in Svelte
Install bootstrap\n
Stop the server and run
`npm install bootstrap`
After install, copy the `bootstrap.min.css` from node modules to the **static** folder.
Note: this procees can be automated using `vite` or `rollup`
		
On the root htm import the css `<link rel="stylesheet" href="%sveltekit.assets%/bootstrap.min.css">`

### Layouts
Helps define the layout of your application. eg. A header that will be rendered across all pages.



### Styling
Add style to your html using normal `<style></style>` tag withing your component. The rules are scoped to the component. eg
`svelte
    <p>This is a paragraph.</p>

    <style>
        /* Write your CSS here */
        p {
            color: goldenrod;
            font-family: 'Comic Sans MS', cursove;
            font-size: 2em;
        }
    </style>
You wont be able to change `p` element in othe component.

> Component names are always capitalised, to distinguish them from HTML elements.

### Render HTML in a Component
use `{@html ...} tag` to render html in a component
```svelte
    <script>
        let text = "Hello, from the <strong> Svelte component</strong>"
    </script>
```

To render it on `+page.svelte` <p>`{@html text}`</p>

>**Note:**  Warning! Svelte doesn't perform any sanitization of the expression inside {@html ...} before it gets inserted into the DOM. 

## Reactivity
In the context of a **UI framework**, reactivity means that the framework can automatically __update the DOM__ when the state of any component is changed.
In Svelte.reactivity is triggered by assigning a new value to any top-level variable in a component.
1. Assignments
To add reactivity on your app, use an event listener
example
```svelte
    <script>
        let count = 0
        function increment() {
            count += 1;
        }
    </script>
    <button on:click={increment}>
        Clicked {count}
        {count} === 1? 'time' : 'times';
    </button>
```
2. Declaration
Svelte automatically updates the DOM when your component's state changes. Some parts of the component's state require to be computed from other parts eg. (fullName derived from firstName and lastName), and recomputed whenever they change.
For those components we use `reactive declarations` & as follows: `let count = 0; $: doubled = count * 2;`
If a reactive statement consists entirely of an assignment to an undeclared variable, Svelte will inject a `let` declaration on your behalf.
```svelte
    <script>
        let count = 0;
        // reactive value
        $: doubled = count * 2;
        function increment() { 
            count += 1;
        }
    </script>
    <button on:click={increment}>
        Clicked {count}
        {count === 1 ? 'time' : 'times'}
    </button>
    <p>{count} doubled is {doubled} </p>
```
$: double = count * 2 could also be achieved using {count * 2}
_reactive values are valuable when you need to reference them multiple times or you have values that depend on other reactive values._
>**Note:** reactive declarations and statements will run after other script code and before component markup is rendered.

3. Statements
Run arbitrary statements reactively.
eg. log _count_ whenever the value changes
```svelte 
    let count = 0
    $: console.log(the count is ${count});
```
Group statements in a block 
```svelte
    $: {
        console.log(`the count is ${count}`);
        console.log('this will also be logged by console')
        }
    
    $: if(count >= 10){
        alert('count is dangerously high');
        count= 0
    }
```

4. Updateing Arrays and Objects
Because Svelte's reactivity is triggered by assignments, using array methods like  `push` and `splice` won't automatically cause updates.

```svelte
    <script>
        let numbers = [1,2,3,4,5];

        function addNumbers(){
            numbers.push(numbers.length + 1);
            // redudant method
            // number = numbers
            // idomatic method
            numbers = [...numbers, numbers.length + 1];
        }
        $: sum = numbers.reduce((total, currentNumber) => total + currentNumber, 0);
    </script>
    <p>{numbers.join(' + ')} = {sum}</p>
    <button on:click={addNumbers}>Add a Number</button>
```


## Props
They are passed top-down from parent components to children and are used to specify data that the component can consume to inform what it renders in the DOM.
1. Declaring props
`props` (properties) help us to pass data from one component down to its children.
To declare a property(props) in `Svelve` we use `export` keyword.
example:
`App.svelte`
```svelte
    <script>
        import Nested from './Nested.svelte';
    </script>
    <Nested answer={34} />
```
<!-- prop to import Nested.svelte-->
`Nested.svelte`
```svelte
    <script>
        export let answer;
    </script>
<p> The answer is {answer}</p>
```
2. Default Values 
Helps components to have falback values if you create a component without a value.
`Nested.svelte`
```svelte
    <script>
        export let answer = 23;
    </script>
    <p>The answer is {answer}</p>
```
`App.svelte`
```svelte   
    <script>
        import {Nested} from './Nested.svelte'
    </script>
    <Nested answer = {12} />
    <Nested /> <!-- Will default to the default prop propery-->
```
3. Spread props 
If a prop is not referenced, svelte will default to `undefined`. 
Svelte allows you to spread props from an object in your code, to avoid the extra typing.
`<Prop {...item} />`

`Card.svelte`
```svelte
    <script>
        export let title;
        export let description;
        export let imageUrl;
    </script>

<section>
  <h1>
    <img src={imageUrl} alt="Avatar for {title}" />
     {title}
  </h1>

  <p>{description}</p>
</section>
```
`Parent.svelte`
```svelte
    <script>
  import Card from "./Card.svelte";
</script>

<Card
  title="See you later, Alligator"
  imageUrl="https://alligator.io/images/alligator-logo3.svg"
  description="Not so soon, baboon!" />
```
<!-- Use spread -->
```svelte
    <script>
    import Card from "./Card.svelte";

    const items = [
        {
        id: 1
        title: "Pirate",
        description: "Argg!!",
        imageUrl: "https://alligator.io/images/pirate.svg"
        },
        {
        id: 2
        title: "Chef",
        description: "À la soupe!",
        imageUrl: "https://alligator.io/images/chef.svg"
        }
    ];
    </script>

    <!-- Without spread: -->
    {#each items as item}
    <Card
        title={item.title}
        description={item.description}
        imageUrl={item.imageUrl}
    />
    {/each}

    <!-- With spread: -->
    {#each items as item}
    <Card {...item} />
    {/each}
```

## Logic

1. If blocks
Svelte has a way of expressing logic using conditionals and loops.
To conditinally render some markup, render it in some `if` block.

`App.svelte`
```svelte 
    <script>
        let count = 0

        const increment = () => count + 1;
    </script>

    <button on:click={increment}>
        Clicked {count}
        {count === 1? 'time': 'times'}
    </button>
    {#if (count > 10)}
        <p>{count} is greater than 10 </p>
    {/if}
```

2. Else block
   ```svelte
   {#if (count > 10)}
        <p>{count} is greater than 10 </p>
    {:else}
        <p>{count} is between 0 and 10 </p>
    {/if}
    ```
*Note:* A `#` character indicates a _block_ opening _tag_. A `/` indicates a block closing tag. A `:` character indicates a block continuation tag.

4. Else-if block
`else if` help multiple conditions to be chained together.
```svelte 
    {#if count >10}
        <p>{count} is greater than 10 </p>
    {:else if count < 5}
        <p>{count} is less than 5 </p>
    {:else}
        <p>{count} is between 0 and 10 </p>
    {/if}
```

5. Each block 
syntax is
`{#each items as item} ... {/each}`

6. Keyed each block
By default, when you modify the value of an each block, it will add and remove items at the end of the block, and update any values that have changed. 

Examples:
`Thing.svelte`
```svelte
    <script>
	const emojis = {
		apple: '🍎',
		banana: '🍌',
		carrot: '🥕',
		doughnut: '🍩',
		egg: '🥚'
	};

        // the name is updated whenever the prop value changes...
        export let name;

        // ...but the "emoji" variable is fixed upon initialisation
        // of the component because it uses `const` instead of `$:`
        const emoji = emojis[name];
    </script>

    <p>{emoji} = {name}</p>
```
`App.svelte`
```svelte
    <script>
	import Thing from './Thing.svelte';

	let things = [
		{ id: 1, name: 'apple' },
		{ id: 2, name: 'banana' },
		{ id: 3, name: 'carrot' },
		{ id: 4, name: 'doughnut' },
		{ id: 5, name: 'egg' }
	];

	function handleClick() {
		things = things.slice(1);
	}
</script>

<button on:click={handleClick}>
	Remove first thing
</button>

{#each things as thing}
	<Thing name={thing.name} />
{/each}
```
Explanation:
When you click the Remove first thing button, it does not remove the first <Thing> component, but rather the last DOM node. Then it updates the name value in the remaining DOM nodes, but not the emoji, which is fixed when each <Thing> is created.

Instead, we'd like to remove only the first <Thing> component and its DOM node, and leave the others unaffected.
To do that, we specify a   `unique identifier (or "key")` for the each block:

```svelte
{#each things as thing (thing.id)}
    <Thing name={thing.name} />
{/each}
```

>**Note:** You can use any object as the key, as Svelte uses a Map internally — in other words you could do (thing) instead of (thing.id). _Using a string or number is generally safer_


6. Await blocks
In `asychronous` apps where data has to be waited for,  Svelte makes it easy to await the value of promises directly in your markup:

`utils.js`
```javascript
    export async function getRandomNumber() {
    // Fetch a random number between 0 and 100
    // (with a delay, so that we can see it)
    const res = await fetch('/random-number');

    if (res.ok) {
        return await res.text();
    } else {
        // Sometimes the API will fail!
        throw new Error('Request failed');
    }
}
```
`App.svelte`
```svelte
    <script>
	import { getRandomNumber } from './utils.js';

	let promise = getRandomNumber();

	function handleClick() {
		promise = getRandomNumber();
	}
    </script>

    <button on:click={handleClick}>
        generate random number
    </button>

    {#await promise}
        <p>...waiting</p>
    {:then number}
        <p> the number is {number} </p>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
```

## Events

1. DOM Events
you can listen to any DOM event on an element (such as `click or pointermove`) with the `on: directive:`
__syntax__:
```html
    <div on:pointermove={handleMove}>
        The pointer is at {m.x} * {m.y}
    </div>
```

2. Inline handlers
```svelte
    <script>
        let m = { x: 0, y: 0 };

        function handleMove(event) {
            m.x = event.clientX;
            m.y = event.clientY;
        }
    </script>
    <!--on:pointermove={(handleMove)}-->
    <div on:pointermove={(e) => {
        m = {x: e.clientX, y: e.clientY};
    }}>
        The pointer is at {m.x} x {m.y}
    </div>

    <style>
        div {
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            padding: 1rem;
        }
    </style>

```

3. Event modifiers
DOM event handlers can have modifiers that __alter their behaviour__. For example, a handler with a `once` modifier will only run a single time:

```svelte
    <button on:click|once={() => alert('Hello')}>
        Click Me!
    </button>
```
3.1 Svelte List of modifiers
    3.1.0 `preventDefault` — calls event.preventDefault() before running the handler. Useful for client-side form handling, for example.
    3.1.1 `stopPropagation` — calls event.stopPropagation(), preventing the event reaching the next element
    3.1.2 `passive` — improves scrolling performance on touch/wheel events (Svelte will add it automatically where it's safe to do so)
    3.1.3 `nonpassive` — explicitly set passive: false
    3.1.4 `capture` — fires the handler during the capture phase instead of the bubbling phase
    3.1.5 `once` — remove the handler after the first time it runs
    3.1.6 `self` — only trigger handler if event.target is the element itself
    3.1.7 `trusted` — only trigger handler if event.isTrusted is true, meaning the event was triggered by a user action rather than because some JavaScript called element.dispatchEvent(...)
>You can chain modifiers together, e.g. on:click|once|capture={...}.

4. Component events
components can also dispatch events. to do so, they must create an `event dispatcher`

`Inner.svelte`
```svelte
    <script>
	    import {createEventDispatcher} from 'svelte'
        
        const dispatch = createEventDispatcher()
        
        function sayHello() {
            dispatch('message', {
                text: 'Hello!'
            });
        }
    </script>

    <button on:click={sayHello}>
        Click to say hello
    </button>

```
`App.svelte`
```svelte
    <script>
	    import Inner from './Inner.svelte';

        function handleMessage(event) {
            alert(event.detail.text);
        }
    </script>

    <Inner on:message={handleMessage}/>

```
>*Note: `createEventDispatcher` must be called when the component is first instantiated — you can't do it later inside e.g. a setTimeout callback. This links dispatch to the component instance.

5. Event forwarding
Unlike DOM events, component events don't `bubble`. If you want to listen to an event on some deeply nested component, the intermediate components must forward the event.

__This section needs revisiting😞__

6. DOM event forwarding
--..--

## Binding 
1. Text inputs 
Data flow in Svelte is `top-down`-  a parent component can set props on a child component, and a component can set attributes on an element, but not the other way around.
##### _breaking the rule
Take the case of the `<input>` element in this component — we could add an `on:input` event handler that sets the value of name to `event.target.value`. It gets even worse with other form elements, as we'll see.

Instead, we can use the `bind:value` directive:
`<input bind:value={name}>`

2. Numeric inputs
Everything is a `string` value in the DOM which means you'll have to `coerce` `input.value` before using it.With Svelte `bind:value:` type coercion is taken care of out of the box.
```svelte
    <script>
	let a = 1;
	let b = 2;
    </script>

    <label>
        <input type="number" bind:value={a} min="0" max="10" />
        <input type="range" bind:value={a} min="0" max="10" />
    </label>

    <label>
        <input type="number" bind:value={b} min="0" max="10" />
        <input type="range" bind:value={b} min="0" max="10" />
    </label>

    <p>{a} + {b} = {a + b}</p>
```

3. Checkbox inputs
Checkboxes are used for toggling between states. Instead of binding to `input.value`, we bind to `input.checked:`
`<input type="checkbox" bind:checked={yes} />`

4. Select bindings 
```svelte
        <script>
        let questions = [
            {
                id: 1,
                text: `Where did you go to school?`
            },
            {
                id: 2,
                text: `What is your mother's name?`
            },
            {
                id: 3,
                text: `What is another personal fact that an attacker could easily find with Google?`
            }
        ];

        let selected;

        let answer = '';

        function handleSubmit() {
            alert(
                `answered question ${selected.id} (${selected.text}) with "${answer}"`
            );
        }
    </script>

    <h2>Insecurity questions</h2>

    <form on:submit|preventDefault={handleSubmit}>
        <select
            bind:value={selected}
            on:change={() => (answer = '')}
        >
            {#each questions as question}
                <option value={question}>
                    {question.text}
                </option>
            {/each}
        </select>

        <input bind:value={answer} />

        <button disabled={!answer} type="submit">
            Submit
        </button>
    </form>

    <p>
        selected question {selected
            ? selected.id
            : '[waiting...]'}
    </p>
```
> **Note** the `<option>` values are objects rather than strings. Svelte doesn't mind.
> if the `initalValue` of the selected is not set, the binding will set it to the default value (the first in the list) automatically.
> until the binding is initialised, `selected` remains `undefined`, so we can't blindly reference e.g. `selected.id` in the template.

5. Group inputs
multiple `type="radio"` or `type="checkbox"` inputs relating to the same value, you can use `bind:group` along with the value attribute. 
Radio inputs in the same group are mutually exclusive; checkbox inputs in the same group form an array of selected values.
```svelte 
    <script>
	let scoops = 1;
	let flavours = [];

	const formatter = new Intl.ListFormat('en', { style: 'long', type: 'conjunction' });
    </script>

    <h2>Size</h2>

    {#each [1, 2, 3] as number}
        <label>
            <input
                type="radio"
                name="scoops"
                value={number}
                bind:group={scoops}
            />

            {number} {number === 1 ? 'scoop' : 'scoops'}
        </label>
    {/each}

    <h2>Flavours</h2>

    {#each ['cookies and cream', 'mint choc chip', 'raspberry ripple'] as flavour}
        <label>
            <input
                type="checkbox"
                name="flavours"
                value={flavour}
                bind:group={flavour}
            />

            {flavour}
        </label>
    {/each}

    {#if flavours.length === 0}
        <p>Please select at least one flavour</p>
    {:else if flavours.length > scoops}
        <p>Can't order more flavours than scoops!</p>
    {:else}
        <p>
            You ordered {scoops} {scoops === 1 ? 'scoop' : 'scoops'}
            of {formatter.format(flavours)}
        </p>
    {/if}
```
6. Slect multiple
A `<select>` element can have a multiple attribute, in which case it will populate an array rather than selecting a single value.
```svelte
    <select multiple bind:value={flavours}>
        {#each ['cookies and cream', 'mint choc chip', 'raspberry ripple'] as flavour}
            <option>{flavour}</option>
        {/each}
    </select>
```
7. Text area input
The `<textarea>` element behaves similarly to a text input in Svelte — use `bind:value:`
`textarea bind:value={value}></textarea>`
use shorthand when names match
`<textarea bind:value></textarea>`

>shorthand form where names match applies to all bindings.

## Lifecycle
components have a cycle that starts when it is __created__ and ends when it is **destroyed**.
Functions that allow you to run code at key moment during component lifecycle.
1. `onMount`
runs after the component is first rendered to the DOM.
2. `beforeUpdate and afterUpdate`
`beforeUpdate` function schedules work to happen immediately before the DOM is updated.
`afterUpdate`    is its counterpart, used for running code once the DOM is in sync with your data.
they're useful for doing things imperatively that are difficult to achieve in a purely state-driven way, like updating the scroll position of an element.

3. `tick`
you can call this function at any time, not just when the component first initialises. 
It returns a promise that resolves as soon as any pending state changes have been applied to the DOM (or immediately, if there are no pending state changes).
it does not update the DOM immediately when a component state is updated. Instead, it waits until the next `microtask` to see if there are any other changes that need to be applied, including in other components.
#### usage
`import {tick} from 'svelte';`

## Stores
A ***store*** is an object with a `subscribe()` method that allows interested parties to be notified whenever the store value changes, and an optional `set()` method that allows you to set new values for the store. 
Svelte provides functions for creating `readable, writable, and derived stores` in the  ___svelte/store___ module.
Data saved in the the store is not persisted so on page refresh the data will be lost.

1. Writable stores
`import { writable } from 'svelte/store';`
a writable store has both `set` and `update` methods in addition to `subscribe`.

example:
`App.svelte`
```javascript
    <script>
	import { count } from './stores.js';
	import Incrementer from './Incrementer.svelte';
	import Decrementer from './Decrementer.svelte';
	import Resetter from './Resetter.svelte';

	let count_value;

    count.subscribe((value) => {
        count_value = value;
    });
    </script>

    <h1>The count is {count_value}</h1>

    <Incrementer />
    <Decrementer />
    <Resetter />
```
`store.js`
```javascript
    import { writable } from 'svelte/store';
    export const count = writable(0);
```
`Incrementer.svelte`
```javascript
    <script>
	import { count } from './stores.js';

	function decrement() {
		// TODO decrement the count
		count.update((y) => {
			// let res = y - 1;
				return  y - 1;

		})
	}
</script>

<button on:click={decrement}>
	-
</button>
```
`Decrementer.svelte`
```svelte 
    <script>
	import { count } from './stores.js';

	function decrement() {
		// TODO decrement the count
		count.update((y) => {
			// let res = y - 1;
				return  y - 1;

		})
	}
</script>

<button on:click={decrement}>
	-
</button>
```
`Reseter.svelte`
```svelte
    <script>
	import { count } from './stores.js';

	function reset() {
		// TODO reset the count
		count.set(0)
	}
</script>

<button on:click={reset}>
	reset
</button>
```

2. Auto-subscriptions
above 🖕 has a subtle bug. _— the store is `subscribed` to, but never `unsubscribed`. If the component was instantiated and destroyed many times, this would result in a memory leak._

`App.svelte` cont..
Add
```javascript
    let count_value;
	const unsubscribe = count.subscribe((value) => {
		count_value = value;
	})
```
>Note: Calling a subscribe method returns an unsubscribe function.
Unsubscribe need to be called `onDestroy lifecycle hook`:
`import { onDestroy } from 'svelte';`
`onDestroy(unsubscribe)`

if your component subscribes to multiple stores, you can reference the store value by prefixing store name using `$` symbol.
`This count is {$count}`
>Note: Auto-subscription only works with store variables that are declared (or imported) at the top-level scope of a component.
> Any name beginning with `$` is assumed to refer to a store value. It's effectively a reserved character — Svelte will prevent you from declaring your own variables with a $ prefix.

3. Readable stores
Not all stores should be writable
> eg. a store representing the mouse postion or user geolocation doesn't make sense to be able to set those values from 'outside'. We use readable stores in such cases.

The first value arguement to `readable` is an intial value, which can be `null` or `undefined`.The second arguement is a `start` that takes a `set` callback and returns a `stop` function.
The __start__ function is called when the store gets its first _subscriber_; **stop** is called when the last subscriber _unsubscribes_.

`store.js`
```javascript
    import { readable } from 'svelte/store';

    export const time = readable(new Date(), function start(set) {
        const interval = setInterval(() => {
            set(new Date());
        }, 1000);

        return function stop() {
            clearInterval(interval);
        };
    });
```
``App.svelte`
```svelte
    <script>
        import { time } from './stores.js';

        const formatter = new Intl.DateTimeFormat(
            'en',
            {
                hour12: true,
                hour: 'numeric',
                minute: '2-digit',
                second: '2-digit'
            }
        );
    </script>

    <h1>The time is {formatter.format($time)}</h1>
```

4. Derived stores
`derived` helps us create a store whose value is based on the value of one or more other stores.

🖕 from abv example, lets calculate the amount of time a page has been opened 

`store.js`
```javascript
....
    const start = new Date();

    export const elapsed = derived(
	time,
	($time) => Math.round($time - start)/1000;
```

`App.svelte`
```svelte
....
	import { time, elapsed } from './stores.js';
    <p>
        This page has been open for
        {$elapsed}
        {$elapsed === 1 ? 'second' : 'seconds'}
    </p>
```

5. Custom stores

`store.js`
use the count store example could include increment, decrement and reset methods and avoid exposing set and update:
```javascript
    import { writable } from 'svelte/store';

    function createCount() {
        const { subscribe, set, update } = writable(0);

        return {
            subscribe,
            increment: () => update((n) => n+1),
            decrement: () => update((n) => n - 1),
            reset: () => set(0)
        };
    }

    export const count = createCount();
```

6. Store bindings
If a store is writable — i.e. it has a set method — you can bind to its value, just as you can bind to local component state.
_example _
exporting a `writable` store name and a `derived store` greeting from `stores.js`. Update the `<input>` element in `App.svelte:`

`store.js`
```javascript
    import { writable, derived } from 'svelte/store';

    export const name = writable('world');

    export const greeting = derived(name, ($name) => `Hello ${$name}!`);
```
`App.svelte`
```svelte
    <script>
        import { name, greeting } from './stores.js';
    </script>

    <h1>{$greeting}</h1>
    <input bind:value={$name} />

    <button on:click={() => $name += '!'}>
        Add exclamation mark!
    </button>
```