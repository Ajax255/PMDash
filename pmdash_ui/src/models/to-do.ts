export default class ToDo {
  text = ''
  id = 0
  isFinished = false

  constructor(text: string, id: number) {
    this.text = text
    this.id = id
  }
}
