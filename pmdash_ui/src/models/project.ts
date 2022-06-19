import { Status } from '../enums/status';

export default class Project {
  title = '';
  subject = '';
  members = [];
  created = new Date();
  status = Status.open;
  tasks = [];
  research = [];
  epics = [];
  stories = [];
  inBackLog = [];
  openTasks = [];
  closedTasks = [];
  inProgressTasks = [];
  inReviewTasks = [];
  testingTasks = [];
  blockedTasks = [];
}
