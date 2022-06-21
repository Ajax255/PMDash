import { v4 as uuidv4 } from 'uuid';
import { Status } from '../enums/status';
import Member from './member';
import Task from './task';

export default class Project {
  title = 'test';
  application = '';
  description = 'test area';
  initials = '';
  pinned = false;
  bgColorClass = '';
  members: Member[] = [];
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
