export default class Car {
    constructor(brand, motor, color) {
      const brandSymbol = Symbol('brand');
      const motorSymbol = Symbol('motor');
      const colorSymbol = Symbol('color');
  
      this[brandSymbol] = brand;
      this[motorSymbol] = motor;
      this[colorSymbol] = color;
  
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
  