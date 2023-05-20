import { Component } from '@angular/core';
import {  Router } from '@angular/router';

@Component({
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  constructor(private route:Router) {

  }
  GoToSimulation(){
    this.route.navigate(['/simulation'])
  }
}
