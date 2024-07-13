import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { SimulationFormComponent } from './simulation-form/simulation-form.component';
import { ContactComponent } from './contact/contact.component';



@NgModule({
  declarations: [
    HomeComponent,
    SimulationFormComponent,
    ContactComponent
  ],
  imports: [
    CommonModule
  ]
})
export class FeaturesModule { }
