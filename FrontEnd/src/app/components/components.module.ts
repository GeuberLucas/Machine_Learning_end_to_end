import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './navbar/navbar.component';
import { ErrorDynamicComponent } from './error-dynamic/error-dynamic.component';



@NgModule({
  declarations: [
    NavbarComponent,
    ErrorDynamicComponent
  ],
  imports: [
    CommonModule
  ],
  exports:[
    NavbarComponent,
    ErrorDynamicComponent
  ]
})
export class ComponentsModule { }
