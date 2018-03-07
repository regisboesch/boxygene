<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;

class CreateContactsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('contacts', function(Blueprint $table)
		{
			$table->integer('id', true);
			$table->integer('title_id')->nullable()->index('fk_users_1_idx');
			$table->string('lastname', 45);
			$table->string('firstname', 45);
			$table->date('birthdaydate');
			$table->integer('weight')->nullable();
			$table->binary('picture')->nullable();
			$table->string('email');
			$table->string('phone', 45)->nullable();
			$table->string('Adress1')->nullable();
			$table->string('Adress2')->nullable();
			$table->string('np', 45)->nullable();
			$table->string('city')->nullable();
			$table->integer('country_id')->nullable()->index('fk_users_2_idx');
			$table->timestamps();
			$table->softDeletes();
		});
	}


	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		Schema::drop('contacts');
	}

}
