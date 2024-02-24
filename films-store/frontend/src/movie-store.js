import {writable} from 'svelte/store'


// export const MovieStore = writable([
//     {id: 1, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 2, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 3, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 4, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 5, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 6, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 7, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 8, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 9, name: 'The God Father', director: 'Francis Ford Coppola'},
//     {id: 10, name: 'The God Father', director: 'Francis Ford Coppola'},
// ])

// Get data frm backedn 
// Set inital state fo []
export const MovieStore = writable([])