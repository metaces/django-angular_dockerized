import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Task } from './task'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = 'http://localhost:81/api';

  constructor(private http: HttpClient) { }

  public getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.API_URL}/task/`);
  }

  public postTask(new_task: Task){
    return this.http.post(`${this.API_URL}/task/`, new_task);
  }

  /**
   * Update Task
   */
  public putTask(the_task: Task) {
    return this.http.put(`${this.API_URL}/task/${the_task.id}/`, the_task);
  }

  /**
   * Delete a Task
   */
  public deleteTask(task_id: number) {
    return this.http.delete(`${this.API_URL}/task/${task_id}`);
  }
}
