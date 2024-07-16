import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './components/navbar/navbar.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { RouterModule } from '@angular/router';



@NgModule({
  declarations: [
    NavbarComponent,
    PageNotFoundComponent
  ],
  exports: [NavbarComponent,
    PageNotFoundComponent],
  imports: [
    CommonModule,
    RouterModule
  ]
})
export class CoreModule { }
