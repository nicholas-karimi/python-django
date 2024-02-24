## Install Svelte
1. `npm create svelte@latest my-app`
2. `cd my-app`
3. `npm install`
   
## Run Svelte
`npm run dev -- --open`

### Svelte Routing
- Svelte Routing is filesystem-based
- On the `src/routes` directory create a directory for the routes you want to route to eg `movies` this will allow me to mavigate to `localhoast:5173/movies`

## Links
In svelte we use the native anchor tags `<a href="/movies/{movie.id}">{movie.name}</a>`

## Detail Page
Svelte Routing uses the following
`route/movies/[slug]` to go a specific page 
So you'll be required to create a [id] folder in the root of your route 

## Load data 
Get data from the url
Now to load that file, a `+page.js` file will be required to be loaded fist

### Svelte Stores
Centrally store data to be used by multiple components