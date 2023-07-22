CREATE TABLE
    cargo (
        cargoID CHAR(36) NOT NULL,
        cargoNombre VARCHAR(30),
        cargoFechaIngreso DATE,
        CONSTRAINT PK_cargo PRIMARY KEY (cargoID)
    );

CREATE TABLE
    departamento (
        departamentoID CHAR(36) NOT NULL,
        departamentoNombre VARCHAR(40),
        CONSTRAINT PK_departamento PRIMARY KEY (departamentoID)
    );

CREATE TABLE
    area (
        areaID CHAR(36) NOT NULL,
        areaNombre VARCHAR(40),
        CONSTRAINT PK_area PRIMARY KEY (areaID)
    );
    
CREATE TABLE
    personal (
        personalRut CHAR(10) NOT NULL,
        personalNombre VARCHAR(30),
        personalGenero VARCHAR(4),
        personalDireccion VARCHAR(50),
        cargoID CHAR(36) NOT NULL,
        departamentoID CHAR(36) NOT NULL,
        areaID CHAR(36) NOT NULL,
        CONSTRAINT PK_personal PRIMARY KEY (personalRUT),
        CONSTRAINT FK_cargo FOREIGN KEY (cargoID) REFERENCES cargo(cargoID),
        CONSTRAINT FK_departamento FOREIGN KEY (departamentoID)
        REFERENCES departamento(departamentoID),
        CONSTRAINT FK_area FOREIGN KEY (areaID) REFERENCES area(areaID)
    );

CREATE TABLE
    cargas (
        cargaRut CHAR(10) NOT NULL,
        cargaNombre VARCHAR(35),
        cargaParentesco VARCHAR(30),
        cargaGenero VARCHAR(4),
        personalRutRelacionCarga CHAR(10) NOT NULL,
        CONSTRAINT PK_carga PRIMARY KEY (cargaRut),
        CONSTRAINT FK_personalRut FOREIGN KEY (personalRutRelacionCarga)
        REFERENCES personal(personalRut)
    );

    
CREATE TABLE
    contactos (
        contactoID CHAR(36) NOT NULL,
        contactoRut CHAR(10) NOT NULL, --CAMBIAR A TIPO UNIQUE
        contactoNombre VARCHAR(35),
        contactoRelacionConPersonal VARCHAR(30),
        personalRutContacto CHAR(10) NOT NULL,
        CONSTRAINT PK_contacto PRIMARY KEY (contactoID),
        CONSTRAINT FK_personalRut_contactos FOREIGN KEY (personalRutContacto)
        REFERENCES personal(personalRut)
    );
    
CREATE TABLE
    telefonosContacto (
        telefonoContactoNumero VARCHAR(15) NOT NULL,
        telefonoContactoID CHAR(36) NOT NULL,
        CONSTRAINT PK_telefonoContacto PRIMARY KEY (telefonoContactoNumero),
        CONSTRAINT FK_contactos FOREIGN KEY (telefonoContactoID)
        REFERENCES contactos(contactoID)
    );
    
CREATE TABLE
    telefonosPersonal (
        telefonoPersonalNumero VARCHAR(15) NOT NULL,
        personalRutDueñoNumero CHAR(10) NOT NULL,
        CONSTRAINT PK_telefonosPersonal PRIMARY KEY (telefonoPersonalNumero),
        CONSTRAINT FK_personalRut_telefonos FOREIGN KEY (personalRutDueñoNumero)
        REFERENCES personal(personalRut)
    );

CREATE TABLE
    usuario (
        usuarioCorreo VARCHAR(35) NOT NULL,
        usuarioNombre VARCHAR(30) NOT NULL,
        usuarioContraseña VARCHAR(100) NOT NULL,
        usuarioTipoPersonal VARCHAR(20) NOT NULL,
        usuarioPersonalRut CHAR(10) NOT NULL,
        CONSTRAINT PK_usuario PRIMARY KEY (usuarioCorreo)
    );

-- Cuenta de Adminisrador predeterminada para insertar nuevos usuarios.

INSERT INTO usuario (usuarioCorreo, usuarioNombre, usuarioContraseña, usuarioTipoPersonal, usuarioPersonalRut)
VALUES ("admin@yury.cl", "admin", "21232f297a57a5a743894a0e4a801fc3", "admin", "11111111-1")

