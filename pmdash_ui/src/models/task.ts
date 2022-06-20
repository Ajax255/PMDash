import { v4 as uuidv4 } from 'uuid';
import { Type } from '../enums/type';
import { Status } from '../enums/status';
import { Priority } from '../enums/priority';

export default class Task {
  uuid = uuidv4();
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
