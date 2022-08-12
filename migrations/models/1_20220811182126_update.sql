-- upgrade --
ALTER TABLE "orders" ADD "repair_type_id" INT NOT NULL;
ALTER TABLE "orders" ADD "device_type_id" INT NOT NULL;
ALTER TABLE "orders" ADD CONSTRAINT "fk_orders_devicety_37964c37" FOREIGN KEY ("device_type_id") REFERENCES "devicetype" ("id") ON DELETE CASCADE;
ALTER TABLE "orders" ADD CONSTRAINT "fk_orders_repairty_fefbf60b" FOREIGN KEY ("repair_type_id") REFERENCES "repairtype" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "orders" DROP CONSTRAINT "fk_orders_repairty_fefbf60b";
ALTER TABLE "orders" DROP CONSTRAINT "fk_orders_devicety_37964c37";
ALTER TABLE "orders" DROP COLUMN "repair_type_id";
ALTER TABLE "orders" DROP COLUMN "device_type_id";
