import { Component } from '@angular/core';

@Component({
  selector: 'app-job-list',
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.css']
})
export class JobListComponent {
  jobs = [
    { title: 'Math Homework', price: 5000, description: 'Solve 10 calculus problems' },
    { title: 'Essay Writing', price: 7000, description: 'Write a 1000-word essay on AI' },
  ];
}
