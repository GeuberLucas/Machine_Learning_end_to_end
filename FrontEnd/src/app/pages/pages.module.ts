import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagesRoutingModule } from './pages-routing.module';
import { HomeComponent } from './home/home.component';
import { SimulationComponent } from './simulation/simulation.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { ButtonModule } from 'primeng/button';


@NgModule({
  declarations: [
    HomeComponent,
    SimulationComponent,
    AboutComponent,
    ContactComponent
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    ButtonModule
  ]
})
export class PagesModule { }
