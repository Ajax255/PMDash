import { Status } from '../enums/status';
import Member from './member';
import Task from './task';

export default class Project {
  _id!:string
  title = '';
  application = '';
  description = '';
  initials = '';
  pinned = false;
  bgColorClass = '';
  members: Member[] = [];
  created = new Date()
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
