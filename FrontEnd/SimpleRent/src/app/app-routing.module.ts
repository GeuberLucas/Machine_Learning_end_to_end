import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './features/home/home.component';
import { SimulationFormComponent } from './features/simulation-form/simulation-form.component';

const routes: Routes = [
  {path:'',component:HomeComponent},
  {path:'simulation',component:SimulationFormComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
