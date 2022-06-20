import { v4 as uuidv4 } from 'uuid';

export default class Memeber {
  uuid = uuidv4();
  name = '';
  handle = '';
  imageUrl = '';
}
