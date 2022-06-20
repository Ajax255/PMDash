import { v4 as uuidv4 } from 'uuid';
import { Status } from '../enums/status';
import Task from './task';

export default class Project {
  uuid = uuidv4();
  title = '';
  subject = '';
  members: string[] = [];
  created = new Date();
  status = Status.open;
  tasks: Task[] = [];
  research: Task[] = [];
  epics: Task[] = [];
  stories: Task[] = [];
  bugs: Task[] = [];
  subTasks: Task[] = [];
  inBackLog: Task[] = [];
  openTasks: Task[] = [];
  closedTasks: Task[] = [];
  inProgressTasks: Task[] = [];
  inReviewTasks: Task[] = [];
  testingTasks: Task[] = [];
  blockedTasks: Task[] = [];
}
