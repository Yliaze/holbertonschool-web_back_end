export default class Car {
    constructor(brand, motor, color) {
      const brandSymbol = Symbol('brand');
      const motorSymbol = Symbol('motor');
      const colorSymbol = Symbol('color');
  
      this._brand = brand;
      this._motor = motor;
      this._color = color;
  
      // Make the symbols private
      Object.freeze(this);
    }
  
    cloneCar() {
        return new this.constructor(
          this[Symbol.for('brand')],
          this[Symbol.for('motor')],
          this[Symbol.for('color')]
        );
      }
  }
  