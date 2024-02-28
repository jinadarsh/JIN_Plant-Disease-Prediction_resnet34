import { ImageStatus } from './constants';

export interface IPlantModel {
  id: string | null;
  status: ImageStatus;
  time:number;
  url: string;
  plant: string;
  disease: string;
}
