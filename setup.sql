CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL,
    `likes` INT NOT NULL
);
ALTER TABLE
    `users` ADD PRIMARY KEY `users_id_primary`(`id`);
CREATE TABLE `items`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `type` INT NOT NULL,
    `owner` BIGINT NOT NULL,
    `material` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `items` ADD PRIMARY KEY `items_id_primary`(`id`);
CREATE TABLE `material_types`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `material_types` ADD PRIMARY KEY `material_types_id_primary`(`id`);
CREATE TABLE `materials`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `owner` BIGINT NOT NULL,
    `type` INT NOT NULL
);
ALTER TABLE
    `materials` ADD PRIMARY KEY `materials_id_primary`(`id`);
ALTER TABLE
    `items` ADD CONSTRAINT `items_owner_foreign` FOREIGN KEY(`owner`) REFERENCES `users`(`id`);
ALTER TABLE
    `items` ADD CONSTRAINT `items_material_foreign` FOREIGN KEY(`material`) REFERENCES `materials`(`id`);
ALTER TABLE
    `materials` ADD CONSTRAINT `materials_owner_foreign` FOREIGN KEY(`owner`) REFERENCES `users`(`id`);
ALTER TABLE
    `materials` ADD CONSTRAINT `materials_type_foreign` FOREIGN KEY(`type`) REFERENCES `material_types`(`id`);