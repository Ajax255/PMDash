import { defineStore } from 'pinia';
import { Filter } from '../enums/filter';
import ToDo from '../models/to-do';

export const useDashboard = defineStore('daseboard', {
  state: () => ({
    // pinnedProjects: [] as
    // todos: [] as ToDo[],
    // filter: Filter.all,
    // nextId: 0,
  }),
  getters: {
    // finishedTodos(state) {
    //   return state.todos.filter((todo) => todo.isFinished)
    // },
    // unfinishedTodos(state) {
    //   return state.todos.filter((todo) => !todo.isFinished)
    // },
    // filteredTodos(): ToDo[] {
    //   if (this.filter === Filter.finished) {
    //     return this.finishedTodos
    //   } else if (this.filter === Filter.unfinished) {
    //     return this.unfinishedTodos
    //   }
    //   return this.todos
    // },
  },
  actions: {
    // any amount of arguments, return a promise or not
    // addTodo(text: string) {
    //   // you can directly mutate the state
    //   this.todos.push({ text, id: this.nextId++, isFinished: false })
    // },
  },
});
