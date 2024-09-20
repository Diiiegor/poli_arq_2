create table inventario_poli.products
(
    id          bigserial not null
        constraint products_pk
            primary key,
    name        varchar   not null,
    description text      not null,
    image       varchar   not null
);

create table inventario_poli.inventory
(
    product_id integer not null
        constraint inventory_pk
            unique,
    stock      integer not null
);
alter table inventario_poli.inventory
    add constraint inventory_products_id_fk
        foreign key (product_id) references inventario_poli.products;

INSERT INTO inventario_poli.products (id, name, description, image) VALUES (1, 'Nike Pegasus 41', 'La amortiguación responsiva de los Pegasus proporciona una pisada enérgica para correr a diario en carretera. Disfruta de un mayor retorno de energía con las unidades Air Zoom dobles y la entresuela de espuma ReactX Foam. Además, la malla diseñada estratégicamente, mejorada en la parte superior, reduce el peso y aumenta la transpirabilidad.', 'https://nikeco.vtexassets.com/arquivos/ids/616659-800-auto?v=638549414010900000&width=800&height=auto&aspect=true');
INSERT INTO inventario_poli.products (id, name, description, image) VALUES (2, 'Air Jordan 5 Retro "El Grito"', 'Estos AJ5 Retro rinden homenaje al discurso que dio inicio a la lucha por la independencia de México. El cuero cortado a láser añade un look mejorado, y los detalles artesanales, como el cuero en relieve, están inspirados en la arquitectura ornamental de México. Las llamas asimétricas de la entresuela se combinan con el cuero de color blanco para ofrecer un look que recuerda a la bandera mexicana. El deubré especial "Viva" combina todos los elementos.', 'https://nikeco.vtexassets.com/arquivos/ids/671594-800-auto?v=638608868683500000&width=800&height=auto&aspect=true');
INSERT INTO inventario_poli.products (id, name, description, image) VALUES (3, 'Air Jordan 3 "Cement Grey"', 'Impecables y supremos, los AJ3 regresan con todo el estilo y la gracia de siempre. El cuero de calidad de la parte superior y la lujosa textura de estampado tipo piel de elefante se combinan con la unidad Nike Air visible en la suela para crear un ícono cómodo para todos los días.', 'https://nikeco.vtexassets.com/arquivos/ids/670972-800-auto?v=638598520532000000&width=800&height=auto&aspect=true');
INSERT INTO inventario_poli.products (id, name, description, image) VALUES (4, 'Nike Calm', 'Disfruta de una experiencia tranquila y cómoda, sin importar a dónde te lleve tu día libre. Confeccionadas con una espuma suave y responsiva, estas chanclas versátiles presentan un diseño minimalista fácil de usar. Además, cuentan con una plantilla texturizada para mantener los pies en su lugar. Ya sea descansando en el sofá, paseando por la ciudad o de vacaciones en la costa, hazlo con un estilo relajado.', 'https://nikeco.vtexassets.com/arquivos/ids/607771-800-auto?v=638549213080230000&width=800&height=auto&aspect=true');
INSERT INTO inventario_poli.products (id, name, description, image) VALUES (5, 'Jumpman MVP', 'Quizá no inventamos el remix, pero al pensar en el material que teníamos para probar, hicimos una versión superfácil. Tomamos elementos de los AJ6, 7 y 8, para convertirlos en un tenis completamente nuevo que rinde homenaje a la primera ronda de 3 campeonatos victoriosos de MJ. Con detalles de cuero, tela y nobuk, estos tenis rinden homenaje a un legado y al mismo tiempo te alientan a construir el tuyo.', 'https://nikeco.vtexassets.com/arquivos/ids/615082-800-auto?v=638549409871300000&width=800&height=auto&aspect=true');


