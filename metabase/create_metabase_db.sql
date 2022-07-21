DO
$do$
BEGIN
   IF EXISTS (
      select usename FROM pg_catalog.pg_user
      WHERE  usename = 'de_user') THEN

      RAISE NOTICE 'Role "de_user" already exists. Skipping.';
   ELSE
      BEGIN   -- nested block
         CREATE USER de_user with encrypted password 'de_pass';
      EXCEPTION
         WHEN duplicate_object THEN
            RAISE NOTICE 'User "de_user" was just created by a concurrent transaction. Skipping.';
      END;
   END IF;
END
$do$;

create database metabase with owner de_user;

grant all privileges on database metabase to de_user;