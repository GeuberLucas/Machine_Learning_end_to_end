import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  navItens: MenuItem[] = [];
  constructor() {}

  ngOnInit(): void {
    this.navItens = [
      { label: 'Inicio' },
      { label: 'Simulação' },
      { label: 'Sobre' },
      { label: 'Contato' },
    ];
  }
}
