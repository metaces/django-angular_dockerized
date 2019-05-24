import { Component, OnInit } from '@angular/core';
import { Observable, from } from 'rxjs'

import { ApiService } from '../api.service'
import { Task } from '../task'

import { FormGroup, FormBuilder } from '@angular/forms'

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  tasks$: Observable<Task[]>;
  task_form: FormGroup;

  constructor(private apiService: ApiService, private form_builder: FormBuilder) { }

  ngOnInit() {
    this.getTasks();
    this.task_form = this.form_builder.group({
      title: '',
      content: ''
    });
  }

  onSubmit() {
    this.apiService.postTask(this.task_form.value)
      .subscribe(
        (response) => {
          console.log(response);
          this.getTasks();
        }
      )
  }
  
  public getTasks() {
    this.tasks$ = this.apiService.getTasks();
  }

}
