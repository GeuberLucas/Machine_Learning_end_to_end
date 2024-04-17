import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from '../layout/layout.component';
import { HomeComponent } from './home/home.component';
import { RentComponent } from './rent/rent.component';

const routes: Routes = [

  {
    path:"",
    component:LayoutComponent,
    children:[{
      path:"",
      component:HomeComponent,
      title:'Home'
    },
    {path:"Rent",component:RentComponent},
    {path:'**',redirectTo:""}
  ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FeaturesRoutingModule { }
