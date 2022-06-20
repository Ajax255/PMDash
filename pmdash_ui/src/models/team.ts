import { v4 as uuidv4 } from 'uuid';

export default class Team {
  uuid = uuidv4();
  name = '';
  href = '';
  bgColorClass = '';
}
