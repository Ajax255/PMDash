import { v4 as uuidv4 } from 'uuid';

export default class Team {
  _id = uuidv4();
  name = '';
  href = '';
  bgColorClass = '';
  members: string[] = [];
}
