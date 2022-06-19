import { Status } from '../enums/status';
import { Type } from '../enums/type';

export default class Task {
  title = '';
  type = Type.task;
  priority = '';
  lables = '';
  sprint = '';
  status = Status.backlog;
  discription = '';
  attachments = [];
  subTaskes = [];
  assigned = '';
  created = new Date();
}
