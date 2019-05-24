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
}
