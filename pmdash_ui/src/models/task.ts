import { Type } from '../enums/type';
import { Status } from '../enums/status';
import { Priority } from '../enums/priority';

export default class Task {
  title = '';
  type = Type.task;
  priority = Priority.low;
  lables = '';
  sprint = '';
  status = Status.backlog;
  discription = '';
  attachments: string[] = [];
  subTaskes: string[] = [];
  assigned = '';
  created = new Date();
  subTasks: Task[] = [];
}
